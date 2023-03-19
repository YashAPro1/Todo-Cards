import React, { useState } from "react";

function CreateArea(props){

    const [note, setNote] = useState({
        title: "",
        content: ""
    });


    function handleChange(event) {
       const { name, value } = event.target;

       setNote(prevNote => {
           return {
               ...prevNote,
               [name] : value
           };
       });
    }

    function submitNote(event){
        props.onAdd(note);
        setNote({
            title: "",
            content: ""
        })
        event.preventDefault();

    }

    return(
        <div classNameName="allform">
            
            

            <div className="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div className="modal-dialog modal-dialog-centered">
                <div className="modal-content">
                <div className="modal-header">
                    <h1 className="modal-title fs-5" id="staticBackdropLabel">Add To List</h1>
                    <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form>
                <div className="modal-body">
                    <input 
                    name="title" 
                    onChange={handleChange} 
                    value={note.title} 
                    placeholder="Title" 
                    />
                    <textarea 
                    onChange={handleChange}
                    name="content" 
                    value={note.content} 
                    placeholder="Take a note..." 
                    rows="3"
                    />
                    
                </div>
                    <div className="modal-footer">
                        <button type="button" className="btn btn-primary"  onClick={submitNote} >Add</button>
                    </div>
                </form>
                </div>
            </div>
            </div>
        </div>
    )
}

export default CreateArea ;


 