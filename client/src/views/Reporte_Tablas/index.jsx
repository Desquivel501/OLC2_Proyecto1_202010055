import React, { useEffect, useState } from "react";
import Table from 'react-bootstrap/Table'

export const Reporte_Tablas = () => {

    const [tabla, setTabla] = useState(null)

    let i = 1

    useEffect(() => {
        getemployees()
    }, [])

    const getemployees = () => {
      fetch("http://127.0.0.1:5000/tablas", {
          method: 'GET',
          headers: {
            'Content-Type':'application/json'
          }
        })
          .then(res => res.json())
          .then(
              (result) => {                    
                setTabla(result)
              },
              (error) => {
                setBase(null);
              }
          )
   }

  if (!tabla) return (<h1 className='text-white mb-4 mt-4'>No se han encontrado tablas</h1>)

  return (
      <div className='justify-content-start'>
        <h1 className='text-white mb-4 mt-4'>Tablas de base de datos</h1>


          <Table striped bordered hover variant="dark">
            <thead>
              <tr>
                <th>No.</th>
                <th>Nombre Tabla</th>
                <th>Nombre base de datos</th>
                <th>Linea</th>
              </tr>
            </thead>
            <tbody>

              {tabla.map(tas => (
                    <tr>
                        <td>{i++}</td>
                        <td>{tas.nombre_tablas}</td>
                        <td>{tas.nombre_base}</td>
                        <td>{tas.linea}</td>
                    </tr>
                ))}
              
            </tbody>
          </Table>


      </div>
    )
  }
  