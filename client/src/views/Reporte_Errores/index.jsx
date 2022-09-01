import React, { useEffect, useState } from "react";
import Table from 'react-bootstrap/Table'

export const Reporte_Errores = () => {

    const [simbolo, setSimbolos] = useState(null)

    useEffect(() => {
        getemployees()
    }, [])

    const getemployees = () => {
      fetch("http://127.0.0.1:5000/errores", {
          method: 'GET',
          headers: {
            'Content-Type':'application/json'
          }
        })
          .then(res => res.json())
          .then(
              (result) => {                    
                setSimbolos(result)
              },
              (error) => {
                setSimbolos(null);
              }
          )
   }

  if (!simbolo) return (<h1 className='text-white mb-4 mt-4'>No se han encontrado simbolos</h1>)

  return (
      <div className='justify-content-start'>
        <h1 className='text-white mb-4 mt-4'>Reporte Tabla de Errores</h1>


          <Table striped bordered hover variant="dark">
            <thead>
              <tr>
                <th>Tipos</th>
                <th>Mensaje</th>
                <th>Ambito</th>
                <th>Linea</th>
                <th>Columna</th>
              </tr>
            </thead>
            <tbody>

              {simbolo.map(sim => (
                    <tr>
                        <td>{sim.tipo}</td>
                        <td>{sim.mensaje}</td>
                        <td>{sim.ambito}</td>
                        <td>{sim.linea}</td>
                        <td>{sim.columna}</td>
                    </tr>
                ))}
              
            </tbody>
          </Table>


      </div>
    )
  }
  