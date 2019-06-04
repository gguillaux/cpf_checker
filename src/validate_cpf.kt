class CPF(cpf_number: String){
    val cpf = cpf_number
    val cpf_clean = clean_cpf(cpf)

    private fun clean_cpf(cpf: String): String{
        val re = Regex("[^\\d]")
        return re.replace(cpf, "")
    }
}

fun main(){
    val c = CPF("378.962.058-07")
    println(c.cpf)
    println(c.cpf_clean)
}