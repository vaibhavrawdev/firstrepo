/* function encodeImageFileAsURL(e) {
    var file = e.files[0];
    var reader = new FileReader();
    reader.onloadend = function() {
      console.log('RESULT', reader.result)
    }
    reader.readAsDataURL(file);
  }
  
  function encodeImageFileAsURL(e) 
{
    return function()
    {
        var file = this.files[0];
        var reader  = new FileReader();
        reader.onloadend = function () 
        {
            e(reader.result);
        }
        reader.readAsDataURL(file);
    }
}
*/
