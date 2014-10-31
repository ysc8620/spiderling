import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
      
public class test {
        private Pattern keyWord=null;  
        /** 
         * @param args 
         */  
        public static void main(String[] args) {  
            Keys k= new Keys("中国人");  
            String sentences="我是中国人。你是日本人!他是美国人.他妈是中国人.";  
            List sentencesResult=k.getSentences(sentences);  
            if(sentencesResult==null){  
                System.out.println("没找到相关的句子");  
                return;  
            }  
            Iterator it =sentencesResult.iterator();  
            for(;it.hasNext();){  
                String str =(String)it.next();  
                System.out.println(str);  
            }  
              
      
        }  
        public Keys(){}  
        public Keys(String key){  
            this.setKeyWord(key);  
        }  
        public String [] sentences(String str){  
            return str.split("[.|;|?|!|！|。|；]");  
        }  
        public void setKeyWord(String keyword){  
            keyWord = Pattern.compile(".*("+keyword+").*");  
        }  
        public List getSentences(String str){  
            List list= new LinkedList();  
            String [] sentences =sentences(str);   
            for(int i=0;i<sentences.length;i++){  
                Matcher m= keyWord.matcher(sentences[i]);  
                if(m.find()){  
                    list.add(sentences[i]);  
                }  
            }  
            if(list.size()==0)return null;  
            return list;  
        }  
    }  