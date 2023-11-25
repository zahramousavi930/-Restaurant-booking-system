let $id = (id) => document.getElementById(id);
var [login, register, form] = ['login', 'register', 'form'].map(id => $id(id));

[login, register].map(element => {
    element.onclick = function () {
        [login, register].map($ele => {
            $ele.classList.remove("active");
        });
        this.classList.add("active");
        this.getAttribute("id") === "register"?  form.classList.add("active") : form.classList.remove("active");
    }
});









//fetch part

function register_data(){
    function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
    const csrftoken = getCookie('csrftoken');

    let   headers={
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        'X-CSRFToken': csrftoken,
}


    const user_email =document.getElementById('r_email').value
    const user_pass =document.getElementById('r_password').value
    const user_username =document.getElementById('r_username').value




    fetch('/user/', {
        method: 'post',
        credentials: 'include',
        headers ,
        body : JSON.stringify({
            user_email,user_pass,user_username
        })
      }).then(response=>{
          response.json()
              .then(res=>{

                  if(res.status === 'exists'){
                      const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 5000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                })

                        Toast.fire({
                    icon: 'error',
                    title: res.message
                })


                  }

                  if(res.status ==='ok'){
                      const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 5000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                })

                        Toast.fire({
                    icon: 'success',
                    title: res.message
                })
                  }
              }) })
}



function login_dataa() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    let headers = {
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        'X-CSRFToken': csrftoken,
    }


    const user_email = document.getElementById('l_email').value
    const user_pass = document.getElementById('l_password').value

    fetch('/user/login',
        {
        method: 'post',
        credentials: 'include',
        headers ,
        body : JSON.stringify({
           user_email,

            user_pass
        }),
         redirect: 'follow'
        }

        ).then(res=>{
        res.json().then(response=>{
            if(response.status === 'no_active'){
                   const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 5000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                })

                    Toast.fire({
                    icon: 'error',
                    title: response.message
                })
            }


            if(response.status === 'no pass'){
                   const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 5000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                })

                    Toast.fire({
                    icon: 'error',
                    title: response.message
                })
            }


             if(response.status === 'ok'){
                 window.location.href = '/'

             }


        })
    })


}