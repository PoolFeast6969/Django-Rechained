console.log("Loaded vote sending");

function vote(direction,id){
    if (isConnected()) {
        window.channel.send('vote',{id: direction});
    } else {
        alert('Soz, cant do that, not connected.');
    }
}
