
// CVolunteer - esentially gets volunteer inputted information
public class CVolunteer {
	public CVolunteer(int volNum, String volName, String phoneNum, int subject, int days, int transportation) {
			volunteerNum=volNum;
			volunteerName=volName;
			PhoneNumber=phoneNum;
			SubjectType=subject;
			DaysType=days;
			TransBool=transportation;
		}
	//gets the inputted subject
	private String getSubjectInString() {
			switch (SubjectType) {
			case 0:
			    return "Math";
			case 1:
			    return "Science";
			case 2:
			    return "History";
			case 3:
			    return "English";
			}
			
			return " ";
		}
	//gets the inputted available days
	private	String getDaysInString() {
			String str = "";
			str += ((DaysType&1)!=0)?"M":"-";
			str += ((DaysType&2)!=0)?"T":"-";
			str += ((DaysType&4)!=0)?"W":"-";
			str += ((DaysType&8)!=0)?"R":"-";

			return str;
		}
	//gets the inputted transportation answer
	private String getTransInString() {
			switch (TransBool) {
			case 0:
			    return "Yes";
			case 1:
			    return "No";
			}
			
			return "Unknown";
		}
	//sets how info will be displayed
	public String getVolunteerInfoLine() {
			return String.format("%08d     %-15s%-20s%-17s%-17s%s",
							volunteerNum, volunteerName, PhoneNumber, getSubjectInString(), getDaysInString(), getTransInString() );
		}

	int volunteerNum;
	String volunteerName;
	String PhoneNumber;
	int SubjectType;
	int DaysType;;
	int TransBool;

}
