$(document).ready
(

		function()
		{
			$("#login").click
			(

				function()
				{
					//console.log('this is step 1')
					var email = $("#username").val();
					var password = $("#password").val();
					//console.log('this is step 5')
					//checking for blank fields
					if( email =='' || password =='')
					{
						console.log('this is step 10')
					 // $('input[type="text"],input[type="password"]').css("border","2px solid red");
					  //$('input[type="text"],input[type="password"]').css("box-shadow","0 0 3px red");
					  alert("Please fill all fields...!!!!!!");
					}
					else
					{
						console.log('this is step 20'+ ", email is: " +email)
						console.log('this is step 30'+ ", password is: " +password)

						$.post
						(
							"checkuname",
							{ username:email, psw:password},
							function(response){
								//var response = $.parseJSON(data);
								console.log('this is step 40')
								console.log(response);
								if(response.success)
								{
									// alert("Post method successful, and user account exist!");
                                    window.location.href = "/searchpage.html";
								}
								else
								{
                  
                                      //alert("Post method successful, but user account does not exist!");
                                      alert("incorrect username or password!");
									
								}
								
							}
						);
					}

				}
			);

		}


);