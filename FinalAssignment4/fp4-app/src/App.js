import './App.css';
import { Outlet } from 'react-router';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, NavDropdown, Container, Nav } from 'react-bootstrap'
import { Provider, useDispatch, useSelector } from 'react-redux'//ini tambahin provider bwt nyimpan data global
import store from './redux-thingy-that-i-stressed';
import { Link } from 'react-router-dom';

function App() {
  return (
    <div>


      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="/">Home</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/readone">Search</Nav.Link>
              <Nav.Link href="/create">Create</Nav.Link>
              <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Never Gonna Give You Up</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">Never Gonna Let You Down</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Never Gonna Make You Cry</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">Never Gonna Desert You</NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <div className="container-app">
        <Provider store={store}>
          <Outlet />
        </Provider>

      </div>
    </div>
  );
}

export default App;
