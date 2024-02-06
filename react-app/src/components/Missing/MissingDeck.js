import React from 'react';
import { useEffect } from 'react';
import Loading from '../LoadingScreen';
import "./MissingUser.css";


const MissingDeck = () => {
    const [showElement,setShowElement] = React.useState(true)
    useEffect(()=>{
      setTimeout(function() {
        return setShowElement(false)
           }, 2000);
         },
      
     [])

    return (
        <>
        {showElement ? (
            <div className='loading-deck'>
                <Loading></Loading>
            </div>
        ) : (
            <h1 className='missing-deck-header'>Deck(s) Could Not Be Found</h1>
        )}
        
        </>
    )
}

export default MissingDeck;