class Student{
    static school_name="WE-school"
    constructor(self,Name,grade){
        this.Name = Name
        this.grade = grade
    }
    display_info(self){
        Console.log(`Name: ${self.Name}, Grade: ${self.grade}, School: ${Student.school_name}`)
    }
}
const student1= Student('Ahmed',90)
student1.display_info()
const student2= Student('Mohamed',90)
student2.display_info()