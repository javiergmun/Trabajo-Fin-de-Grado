const API_URL ="https://jsonplaceholder.typicode.com";

fetch(`${API_URL}/users`)
    .then((response)=>response.json())
    .then((response)=>{
        response.forEach((user)=>{

            const productos = document.createElement('div')
            const dato = document.createElement('div')
            const comentarios = document.createElement('div')

            //---------
            let imagen = document.createElement('img')
            let foto = document.createAttribute('src')
            foto.value='https://definicion.de/wp-content/uploads/2009/06/producto.png'
            imagen.setAttributeNode(foto)

            //let salto= document.createElement('br')
            
            //---------
            let nombre = document.createElement('p')
            let nombreIcono = document.createElement('span')
            nombreIcono.className='fas fa-box '
            nombre.appendChild(nombreIcono)
            nombre.appendChild(
                document.createTextNode(" "+`${user.name}`)
            );
            
            let empresa = document.createElement('p')
            let empresaIcono = document.createElement('span')
            empresaIcono.className='fas fa-user'
            empresa.appendChild(empresaIcono)
            empresa.appendChild(
                document.createTextNode(" "+`${user.username}`)
            );


            let precio = document.createElement('p')
            let precioIcono = document.createElement('span')
            precioIcono.className='fas fa-money-bill'
            precio.appendChild(precioIcono)
            precio.appendChild(
                document.createTextNode(" "+`${user.email}`)
            );


            let mg = document.createElement('i')
            let idMg = document.createAttribute('id')
            idMg.value='meGusta'
            mg.setAttributeNode(idMg)
            mg.append(1)


            let mgIcono = document.createElement('span')
            let funcionMg = document.createAttribute('onclick')
            let idIconoMg = document.createAttribute('id')
            idIconoMg.value='iconoMeGusta'
            funcionMg.value='doLike()'
            mgIcono.setAttributeNode(funcionMg)
            mgIcono.setAttributeNode(idIconoMg)
            mgIcono.className='fas fa-heart '
    
            //---------

            let textComentarios = document.createElement('p')
            let comentariosIcono = document.createElement('span')
            comentariosIcono.className='fas fa-comment'
            textComentarios.appendChild(comentariosIcono)
            textComentarios.appendChild(
                document.createTextNode(" ")
            )
            textComentarios.appendChild(
                document.createTextNode("Comentarios: ")
            );
            //---------

            let botonComentar = document.createElement('input')
            let tipo = document.createAttribute('type')
            let nombreBoton = document.createAttribute('value')
            tipo.value='button',
            nombreBoton.value="Comentar"
            botonComentar.setAttributeNode(tipo)
            botonComentar.setAttributeNode(nombreBoton)


            fetch(`${API_URL}/users`)
                .then((response)=>response.json())
                .then((response)=>{
                    response.forEach((comentary)=>{

                    
                    const comentario = document.createElement('div')

                    let usuarioPost = document.createElement('p')
                    usuarioPost.appendChild(
                    document.createTextNode(`${comentary.website}`)
                    );

                    let valoracion = document.createElement('p')
                    valoracion.appendChild(
                    document.createTextNode(`${comentary.email}`)
                    );

                    comentario.appendChild(usuarioPost)
                    comentario.appendChild(valoracion)

                    comentarios.appendChild(comentario)

                    comentario.className='comentario'
                    
            });
            //---------

            //dato.appendChild(nombreIcono)
            dato.appendChild(nombre)
            dato.appendChild(empresa)
            dato.appendChild(precio)
            dato.appendChild(mgIcono)
            dato.appendChild(mg)
            

        
            productos.appendChild(imagen)
            productos.appendChild(dato)
            productos.appendChild(textComentarios)
            productos.appendChild(comentarios)
            productos.appendChild(botonComentar)

            

            //---------
            botonComentar.className = 'boton-comentar'
            comentarios.className = 'comentarios'
            imagen.className = 'foto-producto'
            dato.className = 'datos'
            productos.className= 'producto'

            
            document.body.appendChild(productos);
        })

            
    });
})

function doLike(){
    var demo = document.getElementById("meGusta");
    var demoValue = parseInt(demo.innerHTML);
    var puntos = demoValue + 1;
    demo.innerHTML = puntos;
}
