
import java.awt.Color;
import java.awt.Container;
import java.awt.event.*;

import javax.swing.*; 

public class Main extends JDialog implements ActionListener {
	//setting all labels, text boxes, etc
	private JLabel label1;
	private JLabel lbVolunteerNum;
	private JLabel label2;
	private JTextField tbVolunteerName;
	private JLabel labelX;
	private JTextField tbPhoneNumber;
	
	private JLabel label3;
	private ButtonGroup  subjectGroup;
	private JRadioButton rbEnglish;
	private JRadioButton rbHistory;
	private JRadioButton rbSciences;
	private JRadioButton rbMath;

	
	private JLabel label5;
	private JCheckBox cbThursday;
	private JCheckBox cbWednesday;
	private JCheckBox cbTuesday;
	private JCheckBox  cbMonday;

	private JLabel label6;
	private ButtonGroup boolGroup;
	private JRadioButton rbNo;
	private JRadioButton rbYes;

    private JButton okButton = null;
    private JButton cancelButton = null;
    
    private boolean cancelled=true;
    public boolean isCancelled() { return cancelled; }
    private CVolunteer answer;
    public CVolunteer getAnswer() { return answer; }

    public Main(JFrame owner, String title, CVolunteer ord) {
		super(owner, title, true);
		//creating the actual display box and all parts within such as buttons, checkboxes, textboxes, and labels
	    Container c = getContentPane();
	    c.setLayout(null);		

	    label1 = new JLabel("Volunteer No.:");
		label1.setSize( 100, 20 );
		label1.setLocation( 40, 40 );
		c.add(label1);

		lbVolunteerNum = new JLabel(String.format("%08d", ord.volunteerNum));
		lbVolunteerNum.setForeground(Color.blue);
		lbVolunteerNum.setSize( 80, 20 );
		lbVolunteerNum.setLocation( 130, 40 );
		c.add(lbVolunteerNum);

		label2 = new JLabel("Volunteer Name:");
		label2.setSize( 100, 20 );
		label2.setLocation( 40, 90 );
		c.add(label2);
		
		tbVolunteerName = new JTextField(ord.volunteerName);
		tbVolunteerName.setSize( 120, 20 );
		tbVolunteerName.setLocation( 140, 90 );
		c.add(tbVolunteerName);


		labelX = new JLabel("Phone Number:");
		labelX.setSize( 100, 20 );
		labelX.setLocation( 300, 90 );
		c.add(labelX);
		
		tbPhoneNumber = new JTextField(ord.PhoneNumber);
		tbPhoneNumber.setSize( 120, 20 );
		tbPhoneNumber.setLocation( 395, 90 );
		c.add(tbPhoneNumber);

	    int x, y;
	    int w, h;	    
		x=40;
		y=150;
	    w=100;
	    h=20;
	    label3 = new JLabel("Subject");
		label3.setSize( 85, 13 );
		label3.setLocation( x, y );
		c.add(label3);

		rbMath = new JRadioButton("Math", ord.SubjectType==0);
		rbMath.setSize( w, h );
		rbMath.setLocation( x+16, y+30 );
		c.add(rbMath);

		rbSciences = new JRadioButton("Sciences", ord.SubjectType==1);
		rbSciences.setSize( w, h );
		rbSciences.setLocation( x+16, y+66 );
		c.add(rbSciences);

		rbHistory = new JRadioButton("History", ord.SubjectType==2);
		rbHistory.setSize( w, h );
		rbHistory.setLocation( x+16, y+102 );
		c.add(rbHistory);

		rbEnglish = new JRadioButton("English", ord.SubjectType==3);
		rbEnglish.setSize( w, h );
		rbEnglish.setLocation( x+16, y+138 );
		c.add(rbEnglish);

		subjectGroup = new ButtonGroup();
		subjectGroup.add(rbEnglish);
		subjectGroup.add(rbHistory);
		subjectGroup.add(rbSciences);
		subjectGroup.add(rbMath);

		x=200;
		y=150;
		w=120;
		h=20;
	    label5 = new JLabel("Days Available");
		label5.setSize( w, h );
		label5.setLocation( x, y );
		c.add(label5);

		cbMonday = new JCheckBox("Monday", (ord.DaysType&1)!=0);
		cbMonday.setSize( w, h );
		cbMonday.setLocation( x+6, y+30 );
		c.add(cbMonday);
		
		cbTuesday = new JCheckBox("Tuesday", (ord.DaysType&2)!=0);
		cbTuesday.setSize( w, h );
		cbTuesday.setLocation( x+6, y+66 );
		c.add(cbTuesday);
		
		cbWednesday = new JCheckBox("Wednesday", (ord.DaysType&4)!=0);
		cbWednesday.setSize( w, h );
		cbWednesday.setLocation( x+6, y+102 );
		c.add(cbWednesday);
		
		cbThursday = new JCheckBox("Thursday", (ord.DaysType&8)!=0);
		cbThursday.setSize( w, h );
		cbThursday.setLocation( x+6, y+138 );
		c.add(cbThursday);

		x=350;
		y=155;
		w=180;
		h=20;
		label6 = new JLabel("Do you need transportation?");
		label6.setSize( 185, 13 );
		label6.setLocation( x, y );
		c.add(label6);
		
		rbYes = new JRadioButton("Yes", ord.TransBool==0);
		rbYes.setSize( w, h );
		rbYes.setLocation( x+12, y+30 );
		c.add(rbYes);

		rbNo = new JRadioButton("No", ord.TransBool==1);
		rbNo.setSize( w, h );
		rbNo.setLocation( x+12, y+66 );
		c.add(rbNo);

		boolGroup = new ButtonGroup();
		boolGroup.add(rbYes);
		boolGroup.add(rbNo);

		cancelButton = new JButton("Cancel");
		cancelButton.addActionListener(this);
		cancelButton.setSize( 100, 50 );
		cancelButton.setLocation( 300, 340 );
		c.add(cancelButton);	

		okButton = new JButton("Submit");
		okButton.addActionListener(this);
		okButton.setSize( 100, 50 );
		okButton.setLocation( 150, 340 );
		c.add(okButton);	
		
	    setSize( 550, 450 );
		setLocationRelativeTo(owner);
		setVisible(true);
    }
    //action listener that performs action based on chosen action
    public void actionPerformed(ActionEvent e) {
		if (e.getSource()==okButton) {
			int volunteerNum=Integer.parseInt(lbVolunteerNum.getText());

			String volunteerName=tbVolunteerName.getText();
			String PhoneNumber=tbPhoneNumber.getText();
			
			int subject=0;
			if (rbMath.isSelected()) subject = 0;
			if (rbSciences.isSelected()) subject = 1;
			if (rbHistory.isSelected()) subject = 2;
			if (rbEnglish.isSelected()) subject = 3;

			int days=0;
			if (cbMonday.isSelected()) days |= 1;
			if (cbTuesday.isSelected()) days |= 2;
			if (cbWednesday.isSelected()) days |= 4;
			if (cbThursday.isSelected()) days |= 8;

			int transportation=0;
			if (rbYes.isSelected()) transportation = 0;
			if (rbNo.isSelected()) transportation = 1;
			
			answer=new CVolunteer(volunteerNum, volunteerName, PhoneNumber, subject, days, transportation);
			
		    cancelled = false;
		    setVisible(false);
		}
		else if(e.getSource()==cancelButton) {
		    cancelled = true;
		    setVisible(false);
		}
    }
    
}
