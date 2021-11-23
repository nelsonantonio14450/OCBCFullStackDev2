
import logo from './logo.svg'
import './App.css'
import { Component } from 'react'
import PersonInformation from './components/PersonInformation'
import FetchComponent from './components/FetchComponent'
import ClockComponent from './components/ClockComponent'
import ClassClock from './components/classClockComp'

export default class App extends Component {

  constructor() {
    super()
    this.state = {
      title: "vercoam to zreatc",
      name: "test",
      scope: {
        manas: "asdasdasd"
      }
    }
  }

  changeTitle = () => {
    this.setState({
      title: "final proj"
    })
  }

  getScope = () => {
    return this.state.scope
  }

  render() {
    return <div className="App">
      <div className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <PersonInformation />
        {/* <FetchComponent /> */}
        <ClockComponent />
        <ClassClock />

      </div>
      <button className="App-Link" onClick={this.changeTitle}>BRUH</button>
      <p className="App-intro">
        Saya belajar dengan tekun supaya bisa menjadi website developer yang hebat.
      </p>
    </div>

  }
}


// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
