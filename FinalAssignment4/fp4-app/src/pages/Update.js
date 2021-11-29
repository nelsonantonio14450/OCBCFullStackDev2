import { useState, useEffect } from "react"
import { useDispatch, useSelector } from 'react-redux'//ini tambahin provider bwt nyimpan data global
import { useParams } from "react-router";
import { Readone_act, update_act } from '../redux-thingy-that-i-stressed/action';
import { Navigate } from 'react-router-dom';


function Create() {
    const { id } = useParams()
    const state = useSelector((state) => state)
    const dispatch = useDispatch()
    useEffect(() => {
        let ignore = false;

        if (!ignore) readone()
        return () => { ignore = true; }
    }, []);

    const [firstName, setFirst] = useState(state.userlist.firstName)
    const [lastName, setLast] = useState(state.userlist.lastName)
    const [redirect, setRedirect] = useState(false)

    const readone = () => {
        dispatch(Readone_act(id))
    }

    const update = () => {
        dispatch(update_act(id, firstName, lastName))
        setRedirect(true)
    }


    return (
        <>
            {redirect ? (<Navigate push to="/" />) : null}
            <form style={{ textAlign: "center", marginTop: "50px" }}>
                <div className="row">
                    <div className="col-sm-3">
                        <h3 style={{ textAlign: "right" }}>First Name:</h3>
                    </div>
                    <div className="col-sm-9">
                        <input style={{ width: "100%", height: "35px" }} defaultValue={state.userlist.firstName} type="text" onChange={(event) => setFirst(event.target.value)} />
                    </div>
                </div>
                <div className="row">
                    <div className="col-sm-3">
                        <h3 style={{ textAlign: "right" }}>Last Name:</h3>
                    </div>
                    <div className="col-sm-9">
                        <input style={{ width: "100%", height: "35px" }} defaultValue={state.userlist.lastName} type="text" onChange={(event) => setLast(event.target.value)} />
                    </div>
                    <br />
                    <div style={{ textAlign: "center" }}>
                        <button className="btn btn-primary" style={{ width: "49%", height: "35px" }} disabled={!state.userlist.firstName && !state.userlist.lastName} type="button" onClick={() => update()}>Update</button>
                    </div>
                </div>
            </form>


            <h3>{state.message}</h3>


        </>

    )
}

export default Create