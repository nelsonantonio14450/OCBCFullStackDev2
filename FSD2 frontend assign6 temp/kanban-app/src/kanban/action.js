export function backlog_act(value) {
    return function (dispatch, getState) {
        var i = 1
        let state = getState()
        var kanbanmap = state.kanbanlist.map(kanban => {
            // [...kanban, { id: 4, title: 'test', status: 1 }]
            // kanban.push({ id: 4, title: 'test', status: 1 })
            i++
            return kanban

        })
        var rickroll = { id: i, title: value, status: 1 }
        dispatch({ type: 'BACKLOG', data: { prevKanban: kanbanmap, value: rickroll } })
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
    return function (dispatch, getState) {
        let state = getState()
        var kanbanmap = state.kanbanlist.map(kanban => {
            if (kanban['id'] === value) {
                kanban.status = "3"
            }
            return kanban
        })
        dispatch({ type: 'EVALUATION', data: kanbanmap })
    }
}


export function done_act(value) {
    return function (dispatch, getState) {
        let state = getState()
        var kanbanmap = state.kanbanlist.map(kanban => {
            if (kanban['id'] === value) {
                kanban.status = "4"
            }
            return kanban
        })
        dispatch({ type: 'DONE', data: kanbanmap })
    }
}

