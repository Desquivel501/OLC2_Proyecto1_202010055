
import { Console } from '../../components/Console';
import { Button } from 'react-bootstrap';
import { useState } from 'react';

import './index.css';

export const Interprete = () => {
  const [code, setCode] = useState('');
  const [consoleText, setConsoleText] = useState('');

  const ejecutar = () => {

    fetch('http://127.0.0.1:5000/interpretar', {
      method: 'POST',
      body: JSON.stringify({instrucciones:code}),
      headers: {
        'Content-Type':'application/json'
      }
    })
      .then(resp => resp.json())
      .then(data => {
        setConsoleText(data.resultado)
      })
      .catch(console.error);
  }

  const clear = () => {
    setConsoleText('');
  }

  return (
    <div className="d-flex fill flex-column justify-content-start">
      <h1 className='text-white mb-4 mt-4'>Interprete</h1>
      <div className='row flex-grow-1'>
        
        <Console code={code} setCode={setCode}>
          <Button
            className='mt-3'
            onClick={ejecutar}
          >Ejecutar</Button>{' '}
        </ Console>

        <Console readOnly code={consoleText} setCode={setConsoleText}>
          <Button
            className='mt-3'
            variant="danger"
            onClick={clear}
          >Clear</Button>{' '}

        </Console>
      </div>
    </div>
  )
}
