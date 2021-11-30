import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux'//ini tambahin provider bwt nyimpan data global
import { delete_act, ReadAll_act } from '../redux-thingy-that-i-stressed/action';
import { Link } from "react-router-dom";
import './readAll.css'


function ReadAll() {
    const state = useSelector((state) => state)
    const dispatch = useDispatch()
    useEffect(() => {
        let ignore = false;
        if (!ignore) readall()
        return () => { ignore = true; }
    }, []);

    // const [loading, setLoading] = useState(true)
    // const [error, setError] = useState(false)

    // useEffect(() => {
    //     console.log('Loading')
    //     readall()
    // }, [])

    // useEffect(() => {
    //     console.log(`Set loading state: ${JSON.stringify(state.userlist)}`)
    //     setLoading(!state.userlist)
    // }, [state.userlist])

    const [open, setOpen] = useState(false);

    const [SerFirNa, setSFN] = useState('');
    const [SerLaNa, setSLN] = useState('');

    const readall = () => {
        dispatch(ReadAll_act())
    }

    const derito = (nama, val) => {

        var r = window.confirm("Delete " + nama + " ?");
        if (r == true) {
            dispatch(delete_act(val))
            readall()
        }
    }

    return (
        <>
            <h1 style={{ textAlign: "center" }}>Daftar User</h1>
            <div style={{ textAlign: "right", marginRight: "30px", marginTop: "25px" }}>
                <label className="switch">
                    <input onChange={() => setOpen(!open)} type="checkbox" />
                    <span className="slider round"></span>
                </label>
            </div>

            {/* {loading ? (<></>) : ( */}
            <table className="table" style={{ textAlign: "center" }}>
                <thead className="thead-dark">
                    <tr>
                        <th scope="col">Key</th>
                        <th scope="col">{!open ? 'First Name' : <input placeholder="Search First Name" onChange={(e) => (setSFN(e.target.value))} />}</th>
                        <th scope="col">{!open ? 'Last Name' : <input placeholder="Search Last Name" onChange={(e) => (setSLN(e.target.value))} />}</th>
                        <th hidden={!open} scope="col">Handle</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        // JSON.stringify(state.userlist)
                        Object.keys(state.userlist).reverse()
                            .filter(test =>
                                state.userlist[test].firstName.includes(SerFirNa) && state.userlist[test].lastName.includes(SerLaNa)
                            ).map((item, i) => (
                                <tr key={i}>
                                    <th style={{
                                        width: "20%",
                                        display: "table-cell"
                                    }} scope="row">{state.userlist[item].key}</th>
                                    <td>{state.userlist[item].firstName}</td>
                                    <td>{state.userlist[item].lastName}</td>
                                    <td hidden={!open}>
                                        <a style={{ marginRight: "10px" }} className="btn btn-warning" href={"/update/" + state.userlist[item].key}> Update </a>
                                        {/* <Link style={{ marginRight: "10px" }} className="btn btn-warning" to={{ pathname: "/update/" + state.userlist[item].key }}> Update </Link> */}
                                        <button className="btn btn-danger" onClick={() => derito(state.userlist[item].lastName, state.userlist[item].key)}> Delete </button>
                                    </td>
                                </tr>


                            ))
                    }
                </tbody>
            </table>

            {/* )} */}





        </>

    )
}

export default ReadAll