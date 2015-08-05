
import java.awt.event.*;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;

import java.awt.*;
import java.util.ArrayList;

public class Test extends JFrame implements ActionListener {
	//creating all labels, buttons, and the list box
	JLabel  myLabel1  = null;
	JLabel  myLabel2  = null;
	JLabel  myLabel3  = null;
	JLabel  myLabel4  = null;
	JLabel  myLabel5  = null;
	JLabel  myLabel6  = null;

	ArrayList<CVolunteer> volunteerArray;
    private DefaultListModel volunteers;
	JList   volunteerList;
	JScrollPane scrollPane = null;
	
	JButton bnAdd = null;
    JButton bnEdit = null;
    JButton bnDel = null;
    JButton bnDelAll = null;
    JButton bnOpen = null;
    JButton bnSave = null;
    
    private JTextField tbFileName;
    
	int volunteerNumber; 

    public Test() {
		super("Volunteers");
		//actually creates/makes visible the things listed above
		Container c = getContentPane();
	    c.setLayout(null);		

	    myLabel1 = new JLabel("Volunteer No.");
		myLabel1.setSize( 200, 50 );
		myLabel1.setLocation( 10, 10 );
		c.add(myLabel1);

	    myLabel2 = new JLabel("Volunteer Name");
		myLabel2.setSize( 200, 50 );
		myLabel2.setLocation( 90, 10 );
		c.add(myLabel2);

	    myLabel3 = new JLabel("Phone No.");
		myLabel3.setSize( 200, 50 );
		myLabel3.setLocation( 215, 10 );
		c.add(myLabel3);

	    myLabel4 = new JLabel("Subject");
		myLabel4.setSize( 200, 50 );
		myLabel4.setLocation( 350, 10 );
		c.add(myLabel4);

	    myLabel5 = new JLabel("Days");
		myLabel5.setSize( 200, 50 );
		myLabel5.setLocation( 460, 10 );
		c.add(myLabel5);
		
	    myLabel6 = new JLabel("Transportation");
		myLabel6.setSize( 200, 50 );
		myLabel6.setLocation( 550, 10 );
		c.add(myLabel6);

	    volunteerArray = new ArrayList<CVolunteer>(); 
		volunteers = new DefaultListModel();
		volunteerList = new JList(volunteers);
	    volunteerList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION );
	    // volunteerList.setFont(new Font("Courier New", Font.PLAIN, 12));
	    volunteerList.setFont(new Font("Monospaced", Font.PLAIN, 12));
	    scrollPane = new JScrollPane(volunteerList);
	    scrollPane.setSize(650, 300);
	    scrollPane.setLocation(10, 50);
	    c.add( scrollPane );
	      
		bnAdd = new JButton("Add");
		bnAdd.setSize( 100, 50 );
		bnAdd.setLocation( 10, 360 );
		bnAdd.addActionListener(this);
		c.add(bnAdd);

		bnEdit = new JButton("Edit");
		bnEdit.setSize( 100, 50 );
		bnEdit.setLocation( 120, 360 );
		bnEdit.addActionListener(this);
		c.add(bnEdit);

		bnDel = new JButton("Delete");
		bnDel.setSize( 100, 50 );
		bnDel.setLocation( 230, 360 );
		bnDel.addActionListener(this);
		c.add(bnDel);

		bnDelAll = new JButton("Clear");
		bnDelAll.setSize( 100, 50 );
		bnDelAll.setLocation( 340, 360 );
		bnDelAll.addActionListener(this);
		c.add(bnDelAll);
		
		bnSave = new JButton("Save");
		bnSave.setSize( 100, 50 );
		bnSave.setLocation( 450, 360 );
		bnSave.addActionListener(this);
		c.add(bnSave);

		bnOpen = new JButton("Open");
		bnOpen.setSize( 100, 50 );
		bnOpen.setLocation( 560, 360 );
		bnOpen.addActionListener(this);
		c.add(bnOpen);

	    setSize( 690, 460 );
	    setLocation( 100, 100 );
	    setVisible(true);

	    volunteerNumber=0;
    }
    //action listener that performs actions based on selected option
    public void actionPerformed(ActionEvent e) {
		if(e.getSource()==bnAdd) {
			volunteerNumber++;
			CVolunteer defaultVolunteer = new CVolunteer(volunteerNumber, "", "", 1, 0, 0); 
		    Main dialogWnd = new Main(this, "Add a Volunteer", defaultVolunteer);
		    if (!dialogWnd.isCancelled()) {
		    	volunteerArray.add(dialogWnd.getAnswer());
		    	volunteers.addElement(dialogWnd.getAnswer().getVolunteerInfoLine());
                volunteerList.setSelectedIndex(volunteers.size()-1);
                volunteerList.ensureIndexIsVisible(volunteers.size()-1);
		    }
		}
	    else if(e.getSource()==bnEdit) {
	    	int index=volunteerList.getSelectedIndex();
	    	if (index>=0) {
			    Main dialogWnd = new Main(this, "Edit a Volunteer", volunteerArray.get(index));
			    if (!dialogWnd.isCancelled()) {
			    	volunteerArray.set(index, dialogWnd.getAnswer());
			    	volunteers.set(index, dialogWnd.getAnswer().getVolunteerInfoLine());
			    }
	    	}
		}
	    else if(e.getSource()==bnDel) {
	    	int index=volunteerList.getSelectedIndex();
	    	if (index>=0) {
			    volunteerArray.remove(index);
			    volunteers.remove(index);
			    if (volunteers.size()>0) {	// not empty
			    	if (index==volunteers.size()) {	// last one deleted
			    		index--;
			    	}
			    	volunteerList.setSelectedIndex(index);
			    	volunteerList.ensureIndexIsVisible(index);
			    }
	    	}
		}
	    else if(e.getSource()==bnDelAll) {
			volunteerArray.clear();
			volunteers.clear();
		}
	    else if(e.getSource()==bnSave) {
	    	JFileChooser chooser = new JFileChooser();
	        FileNameExtensionFilter filter = new FileNameExtensionFilter(
	            "All Files","txt");
	        chooser.setFileFilter(filter);
	        int returnVal = chooser.showSaveDialog(getParent());
	        if(returnVal == JFileChooser.APPROVE_OPTION) {
	           System.out.println("You chose to open this file: " +
	                chooser.getSelectedFile().getName());
	        }
	    }
	    else if(e.getSource()==bnOpen) {
	    	JFileChooser chooser = new JFileChooser();
	        FileNameExtensionFilter filter = new FileNameExtensionFilter(
	            "All Files", "txt");
	        chooser.setFileFilter(filter);
	        int returnVal = chooser.showOpenDialog(getParent());
	        if(returnVal == JFileChooser.APPROVE_OPTION) {
	           System.out.println("You chose to open this file: " +
	                chooser.getSelectedFile().getName());
	        }
       }
    }    
	public static void main(String[] args) {
    	Test mainWnd = new Test();
    }
}
