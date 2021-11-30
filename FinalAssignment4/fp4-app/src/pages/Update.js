import { useState, useEffect } from "react"
import { useDispatch, useSelector } from 'react-redux'//ini tambahin provider bwt nyimpan data global
import { useParams } from "react-router";
import { Readone_act, update_act } from '../redux-thingy-that-i-stressed/action';
import { Navigate } from 'react-router-dom';
import ReadAll from "./ReadAll";


function Create() {
    const { id } = useParams()
    const state = useSelector((state) => state)
    const dispatch = useDispatch()
    // const history = useHistory()


    const [loading, setLoading] = useState(false)

    useEffect(() => {
        let ignore = false;

        if (!ignore) readone()
        return () => { ignore = true; }
    }, []);

    useEffect(() => {
        console.log('Loading')
        readone()
    }, [])

    useEffect(() => {
        console.log(`Set loading state: ${JSON.stringify(state.user)}`)
        setLoading(!state.user)
    }, [state.user])

    const readone = () => {
        dispatch(Readone_act(id))
    }
    const [firstName, setFirst] = useState(state.user.firstName)
    const [lastName, setLast] = useState(state.user.lastName)
    const [redirect, setRedirect] = useState(false)


    const update = () => {
        console.log({ id, firstName, lastName })
        dispatch(update_act(id, firstName, lastName))


        setTimeout(() => {
            window.location.href = '/'
        }, 5000);

    }


    return (

        <>

            {loading ? (<></>) : (
                <form style={{ textAlign: "center", marginTop: "50px" }}>
                    <div className="row">
                        <div className="col-sm-3">
                            <h3 style={{ textAlign: "right" }}>First Name:</h3>
                        </div>
                        <div className="col-sm-9">
                            <input style={{ width: "90%", height: "35px" }} defaultValue={state.user["firstName"]} type="text" onChange={(event) => setFirst(event.target.value)} />
                        </div>
                    </div>
                    <div className="row">
                        <div className="col-sm-3">
                            <h3 style={{ textAlign: "right" }}>Last Name:</h3>
                        </div>
                        <div className="col-sm-9">
                            <input style={{ width: "90%", height: "35px" }} defaultValue={state.user.lastName} type="text" onChange={(event) => setLast(event.target.value)} />
                        </div>
                        <br />
                        <div style={{ textAlign: "center", marginTop: "20px" }}>
                            <button className="btn btn-primary" style={{ width: "29%", height: "35px" }} disabled={!state.user.firstName && !state.user.lastName} type="button" onClick={() => update()}>Update</button>
                        </div>
                    </div>
                </form>


            )
            }
            <h3>{state.message}</h3>

        </>

    )
}

export default Create