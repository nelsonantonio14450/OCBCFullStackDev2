import { createStore, applyMiddleware } from "redux";
import thunk from 'redux-thunk'

const initialState = {
    kanbanlist:
        [
            { id: 1, title: 'Sakit', status: '1' },
            { id: 2, title: 'Pala', status: '2' },
            { id: 3, title: 'Saya', status: '3' }
        ]

}

//reducer
const kanban = (state = initialState, action) => {
    console.log(state)
    switch (action.type) {
        case 'BACKLOG':
            return { kanbanlist: [...action.data.prevKanban, action.data.value] }
        case 'INPROGRESS':
            return { kanbanlist: action.data }
        //operasinya disini kah?


        case 'EVALUATION':
            return { kanbanlist: action.data }

        case 'DONE':
            return { kanbanlist: action.data }

        default:
            return state

    }
}

const enhancer = applyMiddleware(thunk)
//create store
const store = createStore(kanban, enhancer)
export default store