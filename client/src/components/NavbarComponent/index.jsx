import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

import { Link } from "react-router-dom";

export const NavbarComponent = () => {
  return (
    <>

      <Navbar bg="dark" variant="dark">
        <Nav className="justify-content-end">
          <Nav.Item className="ms-4 mt-1">
            <Navbar.Brand as={Link} to="/">
              <img
                alt=""
                src="./src/assets/Rust_Icon_white.png"
                width="30"
                height="30"
                className="d-inline-block align-top"
              />
              {' '}Interprete</Navbar.Brand>
            </Nav.Item> 
            <NavDropdown title="Reportes" id="basic-nav-dropdown">
              <NavDropdown.Item href="/reporte_ts">Reporte de tabla de símbolos</NavDropdown.Item>
              <NavDropdown.Item  href="/errores">Reporte de errores</NavDropdown.Item>
              <NavDropdown.Item href="">Reporte de base de datos existente</NavDropdown.Item>
              <NavDropdown.Item href="">Reporte de tablas de base de datos</NavDropdown.Item>
            </NavDropdown>
            <Nav.Item>
              <Nav.Link as={Link} to="/about">Acerca de</Nav.Link>
          </Nav.Item>
        </Nav>
      </Navbar>

    </>
  )
}
