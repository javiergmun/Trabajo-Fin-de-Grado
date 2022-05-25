const API_URL ="http://127.0.0.1:8000";

fetch(`${API_URL}/productos/moda/`)
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


            fetch(`${API_URL}/productos/moda/`)
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
            productos.appendChild(descripcion)
            productos.appendChild(textComentarios)
            productos.appendChild(comentarios)
            productos.appendChild(botonComentar)

            productos.style.backgroundColor = '#CC72F9';


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

    let inputTituloComent = document.createElement('input')
    let tipoText = document.createAttribute('type')
    tipoText.value='text'
    inputTituloComent.setAttributeNode(tipoText)
    

    let textValoracion = document.createElement('p')
    textValoracion.appendChild(
        document.createTextNode("Valoracion: ")
    );

    let textareavaloracionComent = document.createElement('textarea')

    let botonComentar = document.createElement('input')
    let tipoBot = document.createAttribute('type')
    let nombreBoton = document.createAttribute('value')
    tipoBot.value='submit'
    nombreBoton.value='Confirmar'
    botonComentar.setAttributeNode(tipoBot)
    botonComentar.setAttributeNode(nombreBoton)
    

    let salto1= document.createElement('p')
    let salto= document.createElement('p')



    formulario.appendChild(textTitulo)
    formulario.appendChild(inputTituloComent)
    formulario.appendChild(salto1)
    
    formulario.appendChild(textValoracion)
    formulario.appendChild(textareavaloracionComent)
    formulario.appendChild(salto)

    formulario.appendChild(botonComentar)


    caja.appendChild(formulario)
   
    document.body.appendChild(caja)

    caja.className='caja-comentar'
}
