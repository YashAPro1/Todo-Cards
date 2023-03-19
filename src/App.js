import Navbar from './components/Navbar';
import './App.css';
import React, { useState } from 'react'
import Card from './components/Card';
import Footer from './components/Footer';
import CreateArea from './components/CreateArea';


function App() {
  const [notes, setNotes] = useState([]);

  function addNote(newNote) {
    setNotes(prev => {
      return [...prev, newNote];
    });
  }

  function deleteNote(id){
    setNotes(prev =>{
      return prev.filter((noteItem, index) => {
        return index !== id;
      });
    });
  }

  return (
    <div>
      <Navbar />
      <CreateArea onAdd={addNote} />
      {notes.map((noteItem, index) => {
        return ( 
          <Card 
            key={index}
            id={index}
            title={noteItem.title}
            content={noteItem.content}
            onDelete={deleteNote}
        />
        );
      })}
      
      <Footer />
    </div>
  );
  
}

export default App;
