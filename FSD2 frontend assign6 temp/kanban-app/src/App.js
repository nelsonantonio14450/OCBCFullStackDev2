
import './App.css';
import store from './kanban/kanban';
import { Provider, useDispatch, useSelector } from 'react-redux'//ini tambahin provider bwt nyimpan data global
import { backlog_act, done_act, evaluation_act, inProgress_act } from './kanban/action';



function AppWrapper() {


  return (
    <Provider store={store}>
      <App />
    </Provider>
  );
}

const App = () => {

  const state = useSelector((state) => state)
  const dispatch = useDispatch()

  const backlog = () => {
    dispatch(backlog_act())
  }

  const inProgress = (value) => {
    dispatch(inProgress_act(value))
  }

  const evaluation = () => {
    dispatch(evaluation_act())
  }

  const done = () => {
    dispatch(done_act())
  }
  return (
    <div className="App">

      <div>
        {
          state.kanbanlist.map(kanban => (
            <>
              <li key={kanban['id']}>
                <h3>{kanban['title']} || {kanban['status']}</h3>
                <button onClick={() => inProgress(kanban['id'])}>backlog</button>
              </li>
            </>
          ))
        }
      </div>


    </div>)
}

export default AppWrapper;
