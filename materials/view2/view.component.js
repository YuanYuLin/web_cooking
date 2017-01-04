{% import SPICES('angular') as NG %}
{% call NG.JSMAIN('view2', ['libCore']) %}

    libCore.setMsg("menu_top_title", "Test");
    libCore.setMsg("menu_top_obj", {"title":"View2-2", "list":[{"title":"Item1"},{"title":"Item2"}]});

    var area = document.getElementById('area');
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

    var renderer = new THREE.WebGLRenderer();
    //console.log("Size W:" + area.innerWidth + ", H:" + area.innerHeight);
    //renderer.setSize( window.innerWidth, window.innerHeight );
    renderer.setSize( 1100, 560 );
    area.appendChild( renderer.domElement );

    var geometry = new THREE.BoxGeometry( 1, 1, 1 );
    var material = new THREE.MeshBasicMaterial( { color: 0x11ff33 } );
    var cube = new THREE.Mesh( geometry, material );
    scene.add( cube );

    camera.position.z = 5;

    var render = function () {
        requestAnimationFrame( render );

        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;

        renderer.render(scene, camera);
    };

    render();

{% endcall %}
