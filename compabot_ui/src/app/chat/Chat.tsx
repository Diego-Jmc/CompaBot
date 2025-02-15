"use client"
import React, { useEffect, useRef, useState } from 'react';
import './chat.css'
import MessageBox from '../messageBox/messageBox';
import axios from 'axios';
import QuestionsModal from '../questionsModal/QuestionsModal';

interface ChatProps {

}

interface MessageBoxProps {
    isBot: boolean,
    typewriterEffect: boolean
    message: string

}

interface MessageBoxPropsHour {
    box: MessageBoxProps,
    hour: string
}


const Chat: React.FC<ChatProps> = (props) => {

    // chat history to track all the sent messages
    const [chatHistory, setChatHistory] = useState<MessageBoxPropsHour[]>([])
    const [questionToMake, setQuestionToMake] = useState<string>("")
    const [showQuestionsModal, setShowQuestionsModal] = useState<boolean>(false)

    const msgHistoryContainerRef = useRef<HTMLDivElement>(null);

    function getCurrentHour() {
        return new Date().getHours() + ":" + new Date().getMinutes()
    }

    async function getResponse(question: string): Promise<string> {
        const body = {
            question: question
        };

        try {
            const response = await axios.post(`${process.env.NEXT_PUBLIC_SERVER_URL}/ask`, body);
            if (response.status === 200) {
                console.log(response.data);
                return response.data;
            } else {
                return "Hubo un error procesando tu respuesta.";
            }
        } catch (err) {
            console.error("Error:", err);
            return "Hubo un error procesando tu respuesta.";
        }
    }

    const handleQuestionsModal = (action: boolean) => {
        setShowQuestionsModal(action)
    }

    const handleOnSubmitQuestion = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const newMessage = {
            box: {
                isBot: false,
                typewriterEffect: false,
                message: questionToMake,
            },

            hour: getCurrentHour()
        };

        setChatHistory(prevChatHistory => [...prevChatHistory, newMessage]);

        const response = await getResponse(questionToMake)


        const newChatbotMessage = {
            box: {
                isBot: true,
                typewriterEffect: true,
                message: response
            },
            hour: getCurrentHour()
        };

        //  set all the chats to no typewriter effect to avoid multiple animations
        setChatHistory(prevChatHistory => {
            return [...prevChatHistory.map(e => {
                e.box.typewriterEffect = false
                return e
            }), newChatbotMessage]
        });

        setQuestionToMake("")
    };

    const handleOnChangeQuestion = (event: React.ChangeEvent<HTMLInputElement>) => {
        setQuestionToMake(event.target.value)
    }

    // Scroll down every time there is a now message
    useEffect(() => {
        if (msgHistoryContainerRef.current) {
            msgHistoryContainerRef.current.scrollTo({
                top: msgHistoryContainerRef.current.scrollHeight,
                behavior: 'smooth'
            });
        }
    }, [chatHistory]);

    return (
        <div className="main-chatbox-container">
            <QuestionsModal isOpen={showQuestionsModal} onClose={function (): void {
                handleQuestionsModal(false);
            } }  ></QuestionsModal>
            <div className='tittle'>
                <h1>Try to chat with CompaBot</h1>
                <div className='chat-container'>

                    <div className='msg-history-container' ref={msgHistoryContainerRef}>
                        {chatHistory.map((e, index) => (
                            <MessageBox
                                key={index} // Asegúrate de usar un key único para cada elemento en la lista
                                message={e.box.message}
                                isBot={e.box.isBot}
                                typewriterEffect={e.box.typewriterEffect}
                                hourStr={e.hour}
                            />
                        ))}

                    </div>
                    <form onSubmit={handleOnSubmitQuestion}>
                        <div className='input-box-container'>

                            <input onChange={handleOnChangeQuestion} value={questionToMake} type='text' placeholder='escribe una pregunta'></input>

                            <div className='send-msg-button-container'>
                                <button type='submit' className='void-btn'>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" className="bi bi-arrow-right-square-fill send-msg-button" viewBox="0 0 16 16">
                                        <path d="M0 14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2zm4.5-6.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5a.5.5 0 0 1 0-1" />
                                    </svg>
                                </button>
                            </div>

                        </div>
                    </form>
                </div>
                <button className="basic-btn red-btn" onClick={() => {
                    handleQuestionsModal(true)
                }} >Preguntas disponibles</button>
            </div>

        </div>
    );
};

export default Chat;
