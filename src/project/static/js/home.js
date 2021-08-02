var updateBtns = document.getElementsByClassName('del-subject')
for(i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click', function(){
        var subjectId= this.dataset.subject
        var action= this.dataset.action
        deleteSubject(subjectId, action)


    })
}


function deleteSubject(subjectId, action){
    var url = '/home/delete-registerd-subject'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'subjectId': subjectId, 'action': action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data', data)
    })
    location.reload()
}