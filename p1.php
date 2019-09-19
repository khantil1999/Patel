


<!DOCTYPE html>
<html>
<head>
	<title>student page</title>
</head>
<body>
<h1 align="center">REGISTRATION  FORM</h1>
<table align="center">
<form action=""  method="post" enctype="multipart/form-data"> 
	<tr>
		<td>
			<label for="name">USER NAME:</label>
		</td>
		<td>
			<input type="text" name="name" id="name">
			<span id="s_name" style="color:red ">*</span>
		</td>
	</tr>
	<tr>
		<td>
			<label for="pass">PASSWORD:</label>
		</td>
		<td>
			<input type="password" name="pass" id="pass">
			<span id="s_pass" style="color:red ">*</span>
		</td>
	</tr>
	<tr>
		<td>
			<label for="mob">MOBILE NUMBER :</label>
		</td>
		<td>
			<input type="text" name="mobile" id="mob">
			<span id="s_mobile" style="color:red "></span>
		</td>
	</tr>
	<tr>
		<td>
			<label for="email">EMAIL ADDRESS:</label>
		</td>
		<td>
			<input type="email" name="email" id="email">
			<span id="s_email" style="color:red "></span>
		</td>
	</tr>


	<tr>
		<td>
			<label for="birth">DATE OF BIRTH:</label>
		</td>
		<td>
			<input type="date" name="birth" id="birth">
			<span id="s_birth" style="color:red "></span>
		</td>
	</tr>

	<tr>
		<td>
			<label for="add">ADDRESS:</label>
		</td>
		<td>
			<textarea name="add" id="add"></textarea>
			<span id="s_add" style="color:red "></span>
		</td>
	</tr>
	<tr>
		<td>
		</td>
		<td>
			<input type="button"  name="sub" id="sub" onclick="validate()" value="submit"> 
		</td>
	</tr>	
</form>
	
</table>


<script type="text/javascript">
		function validate()
		{
			// alert("HELLO");
			var u_name=document.getElementById('name').value;
			var pass=document.getElementById('pass').value;
			var mobile=document.getElementById('mob').value;
			var email=document.getElementById('email').value;
			var birth=document.getElementById('birth').value;
			var address=document.getElementById('add').value;
			var letters = /^[A-Za-z]+$/;
			var passc=/^[A-Za-z]+[0-9]+[!@#$%^&*?]$/
			var number=/[0-9]{10}/
			alert(pass);
			if(u_name.length<6)
			{
				document.getElementById('s_name').innerHTML="USER NAME MUST BE GRATER THEN 6 CHARACTERS";
			}
			else if(!u_name.match(letters))
			{
				document.getElementById('s_name').innerHTML="ONLY ALPHABET ARE ALLOWED";	
			}
			else
			{
				document.getElementById('s_name').innerHTML="";		
			}


			if(pass.length<6 || pass.length>12)
			{
				document.getElementById('s_pass').innerHTML="LENGTH MUST BE BETWWEN 8 TO 12";
			}

			else
			{
				document.getElementById('s_pass').innerHTML="";
			}

			if(mobile.length<10 || mobile.match(number))
			{
				document.getElementById('s_mobile').innerHTML="ENTER VALID MOBILE NUMBER";	
			}
			else
			{
				document.getElementById('s_mobile').innerHTML=" ";		
			}

			if(email="")
			{
				document.getElementById('s_email').innerHTML="ENTER VALID MOBILE NUMBER";		
			}



			

		}


</script>

</body>
</html>
