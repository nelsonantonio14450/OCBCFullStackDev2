import { createStore, applyMiddleware, compose } from "redux";
import thunk from 'redux-thunk'

const initialState = {
    userlist: {},
    user: {},
    message: ""

}

//reducer
const users = (state = initialState, action) => {
    // console.log(state)
    switch (action.type) {
        case 'READALL':
            return { userlist: action.data }
        case 'READONE':
            return { user: action.data }
        case 'INSERT':
            return { message: action.data }
        case 'DELETE':
            return state
        default:
            return state

    }
}

// const enhancer = applyMiddleware(
//     [
//         thunk,
//         window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
//     ]
// )

// const composeEnhancers = (window.__REDUX_DEVTOOLS_EXTENSION__) || compose

//create store
const store = createStore(users, compose(
    applyMiddleware(thunk),
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
))
export default store