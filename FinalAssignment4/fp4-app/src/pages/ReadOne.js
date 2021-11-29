import { useState, useEffect } from "react"
import { Readone_act } from "../redux-thingy-that-i-stressed/action"
import { useDispatch, useSelector } from 'react-redux'//ini tambahin provider bwt nyimpan data global

function ReadOne() {
    const state = useSelector((state) => state)
    const dispatch = useDispatch()

    const [search, setSearch] = useState(0)
    // useEffect(() => {
    //     fetch('/keys/' + search).then(res => res.json()).then(data => { setItems(data) }, [search])
    // })

    const readone = () => {
        dispatch(Readone_act(search))
    }


    return (
        <>
            <div>
                <input type="number" onChange={(event) => setSearch(event.target.value)} />
                <button onClick={() => readone()}>one</button>
            </div>

            {
                <>

                    <h1>first name: {state.userlist.firstName}</h1>
                    <h1> last name: {state.userlist.lastName}</h1>
                </>

            }


        </>

    )
}

export default ReadOne