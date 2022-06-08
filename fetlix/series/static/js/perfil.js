const API_URL ="http://127.0.0.1:8000";

const user_id = JSON.parse(document.getElementById('user_id').textContent);


fetch(`${API_URL}/clientes/cliente/${user_id}`)
        .then((response)=>response.json())
        .then((r)=>{
        
            fetch(`${API_URL}/posts/post/cliente/${r.id}`)
            .then((response)=>response.json())
            .then((response)=>{
                response.forEach((comentary)=>{
        
                    
                        let comentario = document.createElement('div')
        
                        let usuarioPost = document.createElement('p')
                        usuarioPost.appendChild(
                            document.createTextNode(`${comentary.producto}`)
                        );
            
                        let valoracion = document.createElement('p')
                        valoracion.appendChild(
                            document.createTextNode(`${comentary.opinion}`)
                        );
            
                        comentario.appendChild(usuarioPost)
                        comentario.appendChild(valoracion)
            
                        
                        comentario.className='comentariosPerfil'
                        document.body.appendChild(comentario);
                             
                            
            });
        })

    })



