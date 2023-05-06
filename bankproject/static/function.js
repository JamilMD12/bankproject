    <script language="javascript" type="text/javascript">
    function dynamicdropdown(listindex)
    {
          document.getElementById("sub-category").length = 0;
                switch (listindex)
        {
        case "kochi" :
            document.getElementById("branch").options[0]=new Option("Select branch","");
            document.getElementById("branch").options[1]=new Option("ALUVA","aluva");
            document.getElementById("branch").options[2]=new Option("KALAMASSERY","kalamassery");
            break;
        case "trivandrum" :
            document.getElementById("branch").options[0]=new Option("Select branch","");
            document.getElementById("branch").options[1]=new Option("POOVVAR,"poovar");
            document.getElementById("branch").options[2]=new Option("KOVALAM","kovalam");

            break;
        case "kollam" :
            document.getElementById("branch").options[0]=new Option("Select branch","");
            document.getElementById("branch").options[1]=new Option("EZHUKONE,"ezhukone");
            document.getElementById("branch").options[2]=new Option("KOTTARAKARA","kottarakara");

            break;
         case "kannur" :
            document.getElementById("branch").options[0]=new Option("Select branch","");
            document.getElementById("branch").options[1]=new Option("KOTTIYOOR,"kottiyoor");
            document.getElementById("branch").options[2]=new Option("THATTADA","thattada");

            break;
           case "wayanad" :
            document.getElementById("branch").options[0]=new Option("Select branch","");
            document.getElementById("branch").options[1]=new Option("EDAKKAL,"edakkal");
            document.getElementById("branch").options[2]=new Option("CHEMBRA","chembra");

            break;
        }
        return true;
    }
    </script>