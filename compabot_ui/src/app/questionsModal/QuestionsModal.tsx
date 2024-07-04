import React, { useEffect, useState } from 'react'
import './questionsModal.css'
import axios from 'axios';

interface QuestionsModalProps {
    isOpen: boolean
    onClose: () => void
}



const QuestionsModal: React.FC<QuestionsModalProps> = ({ isOpen, onClose }) => {

    const [questions, setQuestions] = useState<string[]>([])


    useEffect(() => {
        axios.get(`${process.env.NEXT_PUBLIC_SERVER_URL}/questions`)

            .then(res => {
                if (res.status == 200) {
                    setQuestions(res.data)
                    console.log(res.data)
                }
            })
            .catch(err => {

            })

    },[])

    if (!isOpen) return null
    return (
        <div className="questions-modal-overlay">
            <div className="questions-modal">
                <div className="questions-modal-header">
                    <h2>Preguntas</h2>
                    <button className="close-button basic-btn" onClick={onClose}>Cerrar</button>
                </div>
                <div className="questions-modal-body">
                    {questions.map((e, index) => (
                        <p key={index}>{e}</p>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default QuestionsModal;
