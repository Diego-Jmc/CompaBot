import React from 'react';
import './chatbox.css'

interface MessageBoxProps {
    isBot: boolean,
    typewriterEffect: boolean
    message: string,
    hourStr: string
}

const MessageBox: React.FC<MessageBoxProps> = (props) => {
    return (
        <div>
            <div className={`message-box ${props.isBot ? "chat-pos" : "user-pos"}`}>

                <div>
                    <div className='hour-container'>{props.hourStr}</div>
                    <div className={`msg-content msg ${props.isBot ? "bot-msg" : "user-msg"}`}>
                        <div className={props.isBot && props.typewriterEffect ? "chat-dialog" : ""}>
                            <p>{props.message} </p>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    );
};

export default MessageBox;
