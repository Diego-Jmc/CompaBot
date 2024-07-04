import React from 'react'
import './QuestionsModal.css'

interface QuestionsModalProps {
  isOpen: boolean
  onClose: () => void
}

const QuestionsModal: React.FC<QuestionsModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null
  return (
    <div className="questions-modal-overlay">
      <div className="questions-modal">
        <div className="questions-modal-header">
          <h2>Preguntas</h2>
          <button className="close-button" onClick={onClose}>Cerrar</button>
        </div>
        <div className="questions-modal-body">
          <p>Pregunta 1: Lorem ipsum dolor sit amet?</p>
          <p>Pregunta 2: Consectetur adipiscing elit?</p>
          <p>Pregunta 3: Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua?</p>
        </div>
      </div>
    </div>
  );
};

export default QuestionsModal;
