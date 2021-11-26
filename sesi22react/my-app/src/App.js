import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import styles from './App.css'
import styled from 'styled-components'

function App() {
  // const [placeholder, setPlaceHolder] = useState('Hi');
  // const [paragraphStyle, setParagraphStyle] = useState({
  //   backgroundColor: "#F00"
  // })
  const [paragrahpClass, setParagraphClass] = useState(styles.small)

  const PRed = styled.p`
  font-size: 10pt;
  color: red;
  `

  const PBlue = styled.p`
  font-size: 30pt;
  color: blue;
  `

  // const changeStyle = () => setParagraphStyle({
  //   backgroundColor: "#00F"
  // })

  // const changeStyle = () => setParagraphClass("Paragraph Blue")
  const changeStyle = () => setParagraphClass(styles.large)

  // useEffect(() => {
  //   fetch('/hello').then(res => res.json()).then(data => { setPlaceHolder(data.result) }, [])
  // })

  return (
    <div className="App">
      <header className="App-header">

        <PRed>
          asdasdasd
        </PRed>
        <PBlue>
          asdasdasd
        </PBlue>
        <button onClick={changeStyle}>Change Background Color</button>

      </header>
    </div>
  );
}

export default App;
