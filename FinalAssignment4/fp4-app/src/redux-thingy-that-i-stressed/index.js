import { createStore, applyMiddleware } from "redux";
import thunk from 'redux-thunk'

const initialState = {
    userlist: {},
    message: ""

}

//reducer
const users = (state = initialState, action) => {
    // console.log(state)
    switch (action.type) {
        case 'READALL':
            return { userlist: action.data }
        case 'READONE':
            return { userlist: action.data }
        case 'INSERT':
            return { message: action.data }
        case 'UPDATE':
            return { userlist: action.data }
        case 'DELETE':
            return state
        default:
            return state

    }
}

const enhancer = applyMiddleware(thunk)
//create store
const store = createStore(users, enhancer)
export default store