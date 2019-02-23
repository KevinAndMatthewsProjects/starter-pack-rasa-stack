import java.util.*;
public class HealthAdvice {
	private Random rand = new Random();
	public String getHealthAdvice() {
		String[] advice = new String[]{
			"Limit the amount sugary beverages you drink to prevent obesity and diabetes.",
			"Nuts have high nutritional value and can help you lose weight.",
			"Try to avoid processed junk food since they have low nutritional value.",
			"The US Department of Health and Human Services recommends at least 150 minutes of "
			+ "moderate aerobic activity or 75 minutes of vigorous aerobic activity a week, or"
			+ "a combination of the two.", 
			"Prevent dehydration by drinking at least 2 liters of water everyday!",
			"Be sure to get at least 8 hours of sleep for an energized morning!",
			"Eat vegetables! They contain plenty of vitamins, minerals, and antioxidants!",
			"Avoid smoking to reduce risk of lung cancer.",
			"Reduce intake of red meats to prevent cholesterol buildup."

		};
		return advice[rand.nextInt(advice.length)];
	}
	
	public static void main(String[] args) {
		HealthAdvice health = new HealthAdvice();
		System.out.println(health.getHealthAdvice());
	}
}
