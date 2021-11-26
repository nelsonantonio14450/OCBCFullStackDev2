
import './App.css';
import store from './kanban/kanban';
import { Provider, useDispatch, useSelector } from 'react-redux'//ini tambahin provider bwt nyimpan data global
import { backlog_act, done_act, evaluation_act, inProgress_act } from './kanban/action';
import { useState } from 'react';



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
  const [Title, setTitle] = useState()



  const backlog = () => {

    dispatch(backlog_act(Title))

  }

  const inProgress = (value) => {
    dispatch(inProgress_act(value))
  }

  const evaluation = (value) => {
    dispatch(evaluation_act(value))
  }

  const done = (value) => {
    dispatch(done_act(value))
  }
  return (
    <div className="App">

      <form>
        <input style={{ marginBottom: "30px" }} type="text" onChange={event => setTitle(event.target.value)} />
        <div className="row">
          <div className="col-sm-6" style={{ textAlign: "center" }}>
            <button className="btn btn-warning" style={{ width: "100px", textAlign: "center" }} type="button" onClick={backlog} >Create new Task</button>
          </div>

        </div>
      </form>

      <div>
        {
          state.kanbanlist.map(kanban => (

            <li key={kanban['id']}>
              <h3>{kanban['title']} || {kanban['status']}</h3>
              <button onClick={() => inProgress(kanban['id'])}>backlog</button>
              <button onClick={() => evaluation(kanban['id'])}>eval</button>
              <button onClick={() => done(kanban['id'])}>eval</button>
            </li>

          ))
        }
      </div>


    </div>)
}

export default AppWrapper;
