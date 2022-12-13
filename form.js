document.getElementById("formdata").addEventListener("submit",function(e){
    e.preventDefault();
        first_name=document.getElementById("first_name").value;
        last_name=document.getElementById("last_name").value;
        age=document.getElementById("age").value;
        // if(age<18 || age>65)  alert('Age must be between 18 and 65');
        email=document.getElementById("email").value;
        contact_number=document.getElementById("contact_number").value;
        if (document.getElementById('g1').checked) {
            gender = document.getElementById('g1').value;
        }
        if (document.getElementById('g2').checked) {
            gender = document.getElementById('g2').value;
        } 
        batch_id=document.getElementById("batch_id").value;
        amount=500;
        payment_successful="True";

        const formData=new FormData();
        formData.append('first_name',first_name);
        formData.append('last_name',last_name);
        formData.append('age',age);
        formData.append('email',email);
        formData.append('contact_number',contact_number);
        formData.append('gender',gender);
        formData.append('batch_id',batch_id);
        formData.append('amount',amount);
        formData.append('payment_successful',payment_successful);
        console.log(formData);

        // var myHeaders = new Headers();
        // myHeaders.append("Authorization", "Bearer <api_key>");
        // myHeaders.append("Content-Type", "application/json");

        fetch('http://127.0.0.1:8000',{
            method:'POST',
            body:formData,
            // headers: myHeaders
        })
        .then(response=>response.json())
        .then(data=>{
            console.log('Success:',data);
            document.getElementById("first_name").value = "";
            document.getElementById("last_name").value="";
            document.getElementById("age").value="";
            document.getElementById("email").value = "";
            document.getElementById("contact_number").value = "";
            document.getElementById("g1").checked = false;
            document.getElementById("g2").checked = false;
            document.getElementById("batch_id").value = "";
            document.getElementById("output-message").innerText = "Your details have been successfully registered!"
            setTimeout(function(){ 
                document.getElementById("output-message").style.display = "none";
                 }, 3000);
                setTimeout(function(){ 
                document.getElementById("output-message").style.display = "";
                 }, 3000);
        })
        .catch(error=>{
            console.log('Error:',error);
            console.error('Error:', error);
            document.getElementById("output-message").innerText = "Sorry! There was an error submitting your details. "
            setTimeout(function(){ 
            document.getElementById("output-message").style.display = "none";
            }, 3000);
            setTimeout(function(){ 
            document.getElementById("output-message").style.display = "";
            }, 3000);
        })
});

function completePayment(){
    event.preventDefault()
    document.getElementById("send").disabled=false;
}