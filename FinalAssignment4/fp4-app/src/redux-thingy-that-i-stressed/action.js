

export function insert_act(key, firstName, lastName) {
    return (dispatch) => {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "key": key + '', "firstName": firstName, "lastName": lastName })
        };

        fetch('/keys', requestOptions).then(response => response.json())
            .then(data => {
                if (data.errorMsg == null) {
                    dispatch({ type: 'INSERT', data: "Berhasil Insert" })
                }
                else {
                    dispatch({ type: 'INSERT', data: "gagal insert - Perhatikan IDnya" })
                }
            })
    }
}

export function ReadAll_act() {
    return function (dispatch) {

        fetch('/debug').then(res => {
            res.json().then(data => {
                dispatch({ type: 'READALL', data: data })
            })
        })
    }
}

export function Readone_act(val) {
    return function (dispatch) {

        fetch('/keys/' + val).then(res => {
            res.json().then(data => {
                dispatch({ type: 'READONE', data: data })
            })
        })
    }
}



export function update_act(key, firstName, lastName) {
    return (dispatch) => {
        const requestOptions = {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "key": key + '', "firstName": firstName, "lastName": lastName })
        };

        fetch('/keys/' + key, requestOptions).then(response => response.json())
            .then(data => {
                console.log(data)


            })
    }
}

export function delete_act(key) {
    return (dispatch) => {
        const requestOptions = {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "key": key + '' })
        };

        fetch('/keys/' + key, requestOptions).then(response => response.json())
            .then(data => {

                dispatch({ type: 'DELETE' })

            })
    }
}