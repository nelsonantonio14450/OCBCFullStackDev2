import { createStore, applyMiddleware } from "redux";
import thunk from 'redux-thunk'

const initialState = {
    kanbanlist:
        [
            { id: 1, title: 'asdasdasdasd', status: '1' },
            { id: 2, title: 'asdasdasdasd', status: '2' },
            { id: 3, title: 'asdasdasdasd', status: '3' }
        ]

}

//reducer
const kanban = (state = initialState, action) => {
    console.log(state)
    switch (action.type) {
        case 'INPROGRESS':
            return { kanbanlist: action.data }
            //operasinya disini kah?
            break

        case '':
            break

        case '':
            break

        default:
            return state

    }
}

const enhancer = applyMiddleware(thunk)
//create store
const store = createStore(kanban, enhancer)
export default store