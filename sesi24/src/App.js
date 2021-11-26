
import { Outlet } from 'react-router';
import './App.css';
import { useDispatch, useSelector } from 'react-redux'
import { increment, decrement, set_Counter } from './store/actions';

function App() {

  const state = useSelector((state) => state)
  const dispatch = useDispatch()

  const incrementCounter = () => {
    dispatch(increment())
  }

  const decrementCounter = () => {
    dispatch(decrement())
  }

  const setCounter = (value = 20) => {
    dispatch(set_Counter(state.counter + value))
    // dispatch({
    //   type: "SET_COUNTER", data: state.counter + value
    // })
  }

  return (
    <div className="App">
      <nav>
        <ul>
          <li>Home</li>
          <li>abot</li>
          <li>coktreak</li>
        </ul>
      </nav>
      <div>
        <h3>{state.counter}</h3>
        <button onClick={incrementCounter}>add by 1</button>
        <button onClick={decrementCounter}>min by 1</button>
        <button onClick={() => setCounter(23)}>add by custom</button>
      </div>
      <Outlet />

    </div>
  );
}

export default App;
