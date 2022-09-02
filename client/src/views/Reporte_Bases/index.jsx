import React, { useEffect, useState } from "react";
import Table from 'react-bootstrap/Table'

export const Reporte_Bases = () => {

    const [base, setBase] = useState(null)

    let i = 1

    useEffect(() => {
        getemployees()
    }, [])

    const getemployees = () => {
      fetch("http://127.0.0.1:5000/bases", {
          method: 'GET',
          headers: {
            'Content-Type':'application/json'
          }
        })
          .then(res => res.json())
          .then(
              (result) => {                    
                setBase(result)
                console.log(result)
              },
              (error) => {
                setBase(null);
              }
          )
   }

  if (!base) return (<h1 className='text-white mb-4 mt-4'>No se han encontrado bases de datos</h1>)

  return (
      <div className='justify-content-start'>
        <h1 className='text-white mb-4 mt-4'>Tabla de Bases de Datos Existentes</h1>


          <Table striped bordered hover variant="dark">
            <thead>
              <tr>
                <th>No.</th>
                <th>Nombre</th>
                <th>No. Tablas</th>
                <th>Linea</th>
              </tr>
            </thead>
            <tbody>

              {base.map(bas => (
                    <tr>
                        <td>{i++}</td>
                        <td>{bas.nombre_base}</td>
                        <td>{bas.cantidad}</td>
                        <td>{bas.linea}</td>
                    </tr>
                ))}
              
            </tbody>
          </Table>


      </div>
    )
  }
  