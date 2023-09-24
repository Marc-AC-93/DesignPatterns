class Singleton {
    private static instance: Singleton;
    private data = "";

    private constructor() {
        console.log('[Singleton] Starting instance')
    }

    public static getInstance(): Singleton {
        if(!(Singleton.instance)){
            Singleton.instance = new Singleton()
        }
        return Singleton.instance
    }

    public getData(){
        console.log(`[Data] ${this.data}`)
    }

    public setData(newData: string){
        if(this.data != ""){
            console.log(`[Old data] ${this.data}`)
        }
        this.data = newData
        console.log(`[New data] ${this.data}`)
    }
}

const s1 = Singleton.getInstance()
const s2 = Singleton.getInstance()

s1.setData("test")
s2.getData()
s2.setData("test2")