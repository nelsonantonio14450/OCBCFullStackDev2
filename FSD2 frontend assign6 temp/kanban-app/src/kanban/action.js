export function backlog_act() {
    return (dispatch) => {
        dispatch({ type: '' })
    }
}


export function inProgress_act(value) {
    return function (dispatch, getState) {
        let state = getState()
        //Find index of specific object using findIndex method.    
        // var kanban = state.kanbanlist.find((obj => obj.id == value));
        // var kanban = kanban
        // console.log(value)
        // //Update object's name property.
        // state.kanbanlist[the_id].status = "2"
        var kanbanmap = state.kanbanlist.map(kanban => {
            if (kanban['id'] === value) {
                kanban.status = "2"
            }
            return kanban
        })
        dispatch({ type: 'INPROGRESS', data: kanbanmap })
    }
}

export function evaluation_act(value) {
    return { type: '', data: value }
}


export function done_act() {
    return { type: '' }
}
