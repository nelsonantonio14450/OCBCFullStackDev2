import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux'//ini tambahin provider bwt nyimpan data global
import { delete_act, ReadAll_act } from '../redux-thingy-that-i-stressed/action';
import { Link } from "react-router-dom";


function ReadAll() {
    const state = useSelector((state) => state)
    const dispatch = useDispatch()
    useEffect(() => {
        let ignore = false;

        if (!ignore) readall()
        return () => { ignore = true; }
    }, []);

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


            <table class="table" style={{ textAlign: "center" }}>
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">key</th>
                        <th scope="col">First</th>
                        <th scope="col">Last</th>
                        <th scope="col">Handle</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        Object.keys(state.userlist).reverse().map((item, i) => (
                            <tr key={i}>
                                <th scope="row">{state.userlist[item].key}</th>
                                <td>{state.userlist[item].firstName}</td>
                                <td>{state.userlist[item].lastName}</td>
                                <td><Link style={{ marginRight: "10px" }} className="btn btn-warning" to={{ pathname: "/update/" + state.userlist[item].key }}> Update </Link>
                                    <button className="btn btn-danger" onClick={() => derito(state.userlist[item].lastName, state.userlist[item].key)}> Delete </button>
                                </td>
                            </tr>

                        ))
                    }
                </tbody>
            </table>







        </>

    )
}

export default ReadAll