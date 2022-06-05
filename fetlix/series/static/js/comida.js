const API_URL ="http://127.0.0.1:8000";

fetch(`${API_URL}/productos/comida/`)
    .then((response)=>response.json())
    .then((response)=>{
        response.forEach((user)=>{

            const productos = document.createElement('div')
            const idProductos = document.createAttribute('id')
            idProductos.value='idProductos'
            productos.setAttributeNode(idProductos)

            const dato = document.createElement('div')
            const comentarios = document.createElement('div')

            //---------
            let imagen = document.createElement('img')
            let foto = document.createAttribute('src')
            
            foto.value=user.imagen
            imagen.setAttributeNode(foto)

            //let salto= document.createElement('br')
            
            //---------
            let nombre = document.createElement('p')
            let nombreIcono = document.createElement('span')
            nombreIcono.className='fas fa-box '
            nombre.appendChild(nombreIcono)
            nombre.appendChild(
                document.createTextNode(" "+`${user.nombre}`)
            );
            
            let empresa = document.createElement('p')
            let empresaIcono = document.createElement('span')
            empresaIcono.className='fas fa-user'
            empresa.appendChild(empresaIcono)
            empresa.appendChild(
                document.createTextNode(" "+`${user.empresa}`)
            );


            let precio = document.createElement('p')
            let precioIcono = document.createElement('span')
            precioIcono.className='fas fa-money-bill'
            precio.appendChild(precioIcono)
            precio.appendChild(
                document.createTextNode(" "+`${user.precio}`+" €")
            );


            let mg = document.createElement('i')
            let idMg = document.createAttribute('id')
            idMg.value='meGusta'
            mg.setAttributeNode(idMg)
            mg.appendChild(
                document.createTextNode(" "+`${user.num_likes}`)
            );


            let mgIcono = document.createElement('span')
            let funcionMg = document.createAttribute('onclick')
            let idIconoMg = document.createAttribute('id')
            idIconoMg.value='iconoMeGusta'
            funcionMg.value='doLike()'
            mgIcono.setAttributeNode(funcionMg)
            mgIcono.setAttributeNode(idIconoMg)
            mgIcono.className='fas fa-heart '
    
            //---------

            let descripcion = document.createElement('p')
            let idDescripcion= document.createAttribute('id')
            let descripcionIcono = document.createElement('span')
            idDescripcion.value='descripcion'
            descripcionIcono.className='fas fa-scroll'
            descripcion.appendChild(descripcionIcono)
            descripcion.appendChild(
                document.createTextNode(" "+user.descripcion)
            );
            descripcion.setAttributeNode(idDescripcion)
            descripcion.className='descripcion'
            //---------

            let textComentarios = document.createElement('p')
            let idTextComentarios= document.createAttribute('id')
            let comentariosIcono = document.createElement('span')
            idTextComentarios.value='textComentario'
            comentariosIcono.className='fas fa-comment'
            textComentarios.appendChild(comentariosIcono)
            textComentarios.appendChild(
                document.createTextNode(" Comentarios: ")
            );
            textComentarios.setAttributeNode(idTextComentarios)
            textComentarios.className='textComentario'
            
            //---------

            let botonComentar = document.createElement('input')
            let tipo = document.createAttribute('type')
            let nombreBoton = document.createAttribute('value')
            let clickComentar= document.createAttribute('onclick')
            clickComentar.value= 'crearComentario()'
            tipo.value='button',
            nombreBoton.value="Comentar"
            botonComentar.setAttributeNode(clickComentar)
            botonComentar.setAttributeNode(tipo)
            botonComentar.setAttributeNode(nombreBoton)


            fetch(`${API_URL}/posts/post/`)
                .then((response)=>response.json())
                .then((response)=>{
                    response.forEach((comentary)=>{

                        if(user.nombre == comentary.producto){
                            let comentario = document.createElement('div')

                            let usuarioPost = document.createElement('p')
                            usuarioPost.appendChild(
                            document.createTextNode(`${comentary.cliente}`)
                            );

                            let valoracion = document.createElement('p')
                            valoracion.appendChild(
                            document.createTextNode(`${comentary.opinion}`)
                            );

                            comentario.appendChild(usuarioPost)
                            comentario.appendChild(valoracion)

                            comentarios.appendChild(comentario)
                            comentario.className='comentario'
                        }
                });
            })
            //---------

            //dato.appendChild(nombreIcono)
            dato.appendChild(nombre)
            dato.appendChild(empresa)
            dato.appendChild(precio)
            dato.appendChild(mgIcono)
            dato.appendChild(mg)
            

        
            productos.appendChild(imagen)
            productos.appendChild(dato)
            productos.appendChild(descripcion)
            productos.appendChild(textComentarios)
            productos.appendChild(comentarios)
            productos.appendChild(botonComentar)

            productos.style.backgroundColor = '#E5F559';

            //---------
            botonComentar.className = 'boton-comentar'
            comentarios.className = 'comentarios'
            imagen.className = 'foto-producto'
            dato.className = 'datos'
            productos.className= 'producto'

            
            document.body.appendChild(productos);
        })

            
    });


function doLike(){
    //$( "#iconoMeGusta" ).css('color', 'red');
    var demo = document.getElementById("meGusta");
    var demoValue = parseInt(demo.innerHTML);
    var puntos = demoValue + 1;
    
    demo.innerHTML = puntos;
   

}

function crearComentario(){

    let caja = document.createElement('div')

    let formulario = document.createElement('form')

    let textTitulo = document.createElement('p')
    textTitulo.appendChild(
        document.createTextNode("Titulo de tu comentario: ")
    );

    let productoComent = document.createElement('select')
    let idSelect = document.createAttribute('id')
    idSelect.value='selectProducto'
    productoComent.setAttributeNode(idSelect)
    
    fetch(`${API_URL}/productos/comida/`)
        .then((response)=>response.json())
        .then((response)=>{
        response.forEach((pr)=>{

        let productoOption = document.createElement('option')

        productoOption.append(`${pr.nombre}`);

        productoComent.appendChild(productoOption)
        
        });
    })

    let textValoracion = document.createElement('p')
    textValoracion.appendChild(
        document.createTextNode("Valoracion: ")
    );

    let textareavaloracionComent = document.createElement('textarea')
    let idTextArea= document.createAttribute('id')
    idTextArea.value = 'valoracion'
    textareavaloracionComent.setAttributeNode(idTextArea)

    let botonComentar = document.createElement('input')
    let tipoBot = document.createAttribute('type')
    let nombreBoton = document.createAttribute('value')
    let postComentar= document.createAttribute('onclick')
    postComentar.value= 'postComment()'
    tipoBot.value='submit'
    nombreBoton.value='Confirmar'
    botonComentar.setAttributeNode(tipoBot)
    botonComentar.setAttributeNode(nombreBoton)
    botonComentar.setAttributeNode(postComentar)

    //
    let botonSalir = document.createElement('input')
    let tipoBot1 = document.createAttribute('type')
    let nombreSalir = document.createAttribute('value')
    tipoBot1.value='submit'
    nombreSalir.value='Cancelar'
    botonSalir.setAttributeNode(tipoBot1)
    botonSalir.setAttributeNode(nombreSalir)
    
    //


    let salto1= document.createElement('p')
    let salto= document.createElement('p')



    formulario.appendChild(textTitulo)
    formulario.appendChild(productoComent)
    formulario.appendChild(salto1)
    
    formulario.appendChild(textValoracion)
    formulario.appendChild(textareavaloracionComent)
    formulario.appendChild(salto)

    formulario.appendChild(botonComentar)
    formulario.appendChild(botonSalir)

    caja.appendChild(formulario)

    document.body.appendChild(caja)

    botonComentar.className='boton-confirmar'
    botonSalir.className='boton-cancelar'
    caja.className='caja-comentar'
}
function postComment(){

    /* Para obtener el texto */
    var combo = document.getElementById("selectProducto");
    var selected = combo.options[combo.selectedIndex].text;

    var valoracionPost = document.getElementById("valoracion")

    fetch(`${API_URL}/productos/producto/${selected}`)
        .then((response)=>response.json())
        .then((response)=>{
       
            var raw = JSON.stringify({
                "opinion": valoracionPost.value,
                "producto": response.id
            });
              
            var requestOptions = {
                method: 'POST',
                headers:  {
                  'Content-type': 'application/json',
                  'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjU0NjAxMzQ2LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.GVWvVF4xEgOR5olU_ANYYa_zMSWj0J_N34SuxZynZgM'
               
                },
                body: raw,
                redirect: 'follow'
            };
              
            fetch("http://127.0.0.1:8000/posts/post/", requestOptions)
                .then(response => response.text())
                .then(result => console.log(result))
                .catch(error => console.log('error', error));
        
    })

   
}
