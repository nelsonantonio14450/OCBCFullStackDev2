import { useState, useEffect } from "react"
import { useDispatch, useSelector } from 'react-redux'//ini tambahin provider bwt nyimpan data global
import { insert_act } from '../redux-thingy-that-i-stressed/action';


function Create() {
    const state = useSelector((state) => state)
    const dispatch = useDispatch()

    const [firstName, setFirst] = useState()
    const [lastName, setLast] = useState()
    const [key, setKey] = useState()

    const insert = () => {

        dispatch(insert_act(key, firstName, lastName))
    }

    return (
        <>
            <form style={{ textAlign: "center", marginTop: "50px" }}>
                <div className="row">
                    <div className="col-sm-3">
                        <h3 style={{ textAlign: "right" }}>id key:</h3>
                    </div>
                    <div className="col-sm-9">
                        <input style={{ width: "100%", height: "35px" }} type="number" onChange={(event) => setKey(event.target.value)} />
                    </div>
                </div>
                <div className="row">
                    <div className="col-sm-3">
                        <h3 style={{ textAlign: "right" }}>First Name:</h3>
                    </div>
                    <div className="col-sm-9">
                        <input style={{ width: "100%", height: "35px" }} type="text" onChange={(event) => setFirst(event.target.value)} />
                    </div>
                </div>
                <div className="row">
                    <div className="col-sm-3">
                        <h3 style={{ textAlign: "right" }}>Last Name:</h3>
                    </div>
                    <div className="col-sm-9">
                        <input style={{ width: "100%", height: "35px" }} type="text" onChange={(event) => setLast(event.target.value)} />
                    </div>
                </div>
                <br />
                <div style={{ textAlign: "center" }}>
                    <button className="btn btn-success" style={{ width: "49%", height: "35px" }} type="button" onClick={() => insert()}>insert</button>
                </div>
            </form>


            <h3>{state.message}</h3>


        </>

    )
}

export default Create