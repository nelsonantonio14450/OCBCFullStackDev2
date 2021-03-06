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
            <h2 style={{ textAlign: "center" }}>Search by ID</h2>
            <div style={{ textAlign: "center", marginTop: "50px" }}>
                <input style={{ marginRight: "30px" }} type="number" onChange={(event) => setSearch(event.target.value)} />
                <button className="btn btn-secondary" onClick={() => readone()}>Search by ID</button>
                <div style={{ marginTop: "50px", borderStyle: "inset" }}>
                    <div className="row" style={{ marginTop: "50px" }}>
                        <div className="col-sm-3">
                            <h3 style={{ textAlign: "right" }}>First Name: </h3>
                        </div>
                        <div className="col-sm-6">
                            <h3 style={{ textAlign: "right" }}> {!state.user.firstName ? 'none' : state.user.firstName}</h3>
                        </div>
                    </div>
                    <div className="row" style={{ marginTop: "50px" }}>
                        <div className="col-sm-3">
                            <h3 style={{ textAlign: "right" }}> Last Name:</h3>
                        </div>
                        <div className="col-sm-6">
                            <h3 style={{ textAlign: "right" }}> {!state.user.lastName ? 'none' : state.user.lastName}</h3>
                        </div>
                    </div>
                </div>
            </div>




        </>

    )
}

export default ReadOne