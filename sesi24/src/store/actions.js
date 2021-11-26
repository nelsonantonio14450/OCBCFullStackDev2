export function increment() {

    return (dispatch) => {

        // const response = await fetch('/todos/1')
        // const json = await response.json()


        setTimeout(() => {
            dispatch({ type: 'INCREMENT' })
        }, 5000);

    }
}

export function decrement() {
    return { type: 'DECREMENT' }
}

export function set_Counter(value) {
    return { type: 'SET_COUNTER', data: value }
}