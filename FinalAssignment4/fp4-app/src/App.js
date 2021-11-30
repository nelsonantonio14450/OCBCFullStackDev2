import './App.css';
import { Outlet } from 'react-router';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, NavDropdown, Container, Nav } from 'react-bootstrap'
import { Provider, useDispatch, useSelector } from 'react-redux'//ini tambahin provider bwt nyimpan data global
import store from './redux-thingy-that-i-stressed';
import logo from './bg.gif'

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
                <NavDropdown.Item href="https://youtu.be/qWJ9c-SmyHk">Aqua Crying for straight 6 and a half minutes</NavDropdown.Item>
                <NavDropdown.Item href="https://youtu.be/jETHvZPaAAE">Barbruh Skream</NavDropdown.Item>
                <NavDropdown.Item href="https://youtu.be/aLUKfU2AOBY">Gaudeamus Igitur</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="https://youtu.be/TjID_oXZbzI">Rubia - Paimon</NavDropdown.Item>
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

      <div className="container-app bg-img" style={{ textAlign: "center" }}>

        <img src={logo} style={{ marginTop: "50px", marginBottom: "50px" }} />
      </div>

      <div className="footer">
        <p>&copy; Shiiizzaaaaaaaa -Joseph Joestar</p>
      </div>
    </div>
  );
}

export default App;
